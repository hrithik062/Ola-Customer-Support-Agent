from livekit.agents import Agent, JobContext
from agent_tasks import ConfirmPhoneNumber, AnswerQuery
import logging


class VoiceAgent(Agent):
    def __init__(self, ctx:JobContext):
        super().__init__(instructions="You are a Driver Support Assistant from Ola")
        self.ctx = ctx

    async def on_enter(self) -> None:
        logging.info("Reached On Enter Node")
        print("Reached On Enter Node")
        confirmation = await ConfirmPhoneNumber(chat_ctx=self.chat_ctx, ctx=self.ctx)
        if confirmation:
            query_resolution = await AnswerQuery(self.chat_ctx,self.ctx)

            ## Call Closure Logic
            await self.session.generate_reply(instructions="Provide a closing statement in hindi and inform them you are going to close this call",
                                              allow_interruptions=False)

            ## Commented as the console code doesn't support room closure
            # api_client = api.LiveKitAPI()
            # await api_client.room.delete_room(api.DeleteRoomRequest(
            #     room=self.ctx.job.room.name,
            # ))


