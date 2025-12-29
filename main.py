from livekit.plugins import openai
from livekit.agents import (
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
    BackgroundAudioPlayer,
    AudioConfig,
    BuiltinAudioClip,
)
from voice_agent import VoiceAgent
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from openai.types.beta.realtime.session import InputAudioTranscription
import os
from constants import LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET
from dotenv import load_dotenv

load_dotenv()

os.environ['LIVEKIT_API_KEY'] = LIVEKIT_API_KEY
os.environ['LIVEKIT_URL'] = LIVEKIT_URL
os.environ['LIVEKIT_API_SECRET'] = LIVEKIT_API_SECRET

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    await ctx.wait_for_participant()

    ctx.proc.userdata["phone_number"] = "+919526019424"

    session = AgentSession(
        turn_detection=MultilingualModel(),
        stt=openai.STT(language="hi",model="gpt-4o-mini-transcribe",use_realtime=True),
        llm=openai.realtime.RealtimeModel(
            model="gpt-realtime",
            turn_detection=None,
            input_audio_transcription=InputAudioTranscription(
                language="hi",
                model="gpt-4o-mini-transcribe")),
        use_tts_aligned_transcript=True,
        preemptive_generation=True,
    )
    await session.start(agent=VoiceAgent(ctx=ctx), room=ctx.room)
    background_audio = BackgroundAudioPlayer(
        # play office ambience sound looping in the background
        ambient_sound=AudioConfig(BuiltinAudioClip.OFFICE_AMBIENCE, volume=0.3),
        # play keyboard typing sound when the agent is thinking
        thinking_sound=[
            AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING, volume=0.1),
            AudioConfig(BuiltinAudioClip.KEYBOARD_TYPING2, volume=0.1),
        ],
    )
    await background_audio.start(room=ctx.room, agent_session=session)

if __name__ == "__main__":
    # Start background SQS scheduler
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint,
                              initialize_process_timeout=90,load_threshold=0.9))
