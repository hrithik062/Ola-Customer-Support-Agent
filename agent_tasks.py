from livekit.agents import AgentTask, function_tool, llm, StopResponse
import logging

class ConfirmPhoneNumber(AgentTask[bool]):
    def __init__(self, chat_ctx=None, ctx=None):
        super().__init__(
            instructions="""
            Confirm whether the number called by user is registered number 
            and check whether the number is blocked or not
            """,
            chat_ctx=chat_ctx,
        )
        self.ctx = ctx
        self.turn_count = 0

    @staticmethod
    def confirm_number(number): ## Can use a dynamic option to confirm the number
        return True

    async def on_user_turn_completed(
        self, turn_ctx: llm.ChatContext, new_message: llm.ChatMessage
    ) -> None:
        logging.info(f"User turn completed: {new_message.text_content}")
        print(f"User turn completed: {new_message.text_content}")
        if self.turn_count == 0:
            self.ctx.proc.userdata["init_message"] = new_message.text_content
            await self.session.generate_reply(
                instructions="""Provide an Introduction like this - Ola customer support mein
                 aapka swagat hai. Kya yeh aapka registered number hai?""") ## Can Use an Audio here to save up the costing and better consistency
            self.turn_count += 1
            raise StopResponse()
        else:
            self.turn_count += 1


    @function_tool
    async def check_phone_number(self):
        """Use this to check whether user is calling from registered phone number and whether his number is blocked or not"""
        phone_number = self.ctx.proc.userdata["phone_number"]
        if self.confirm_number:
            await self.session.generate_reply(instructions="""Just Inform user that his number is not blocked with this sentence
                         - Aapka number blocked nahi hai. Sab theek hai.""")
            return self.complete(True)
        else:
            return self.complete(False)



    async def on_enter(self) -> None:
        pass


class AnswerQuery(AgentTask[bool]):
    def __init__(self, chat_ctx=None, ctx=None):
        super().__init__(
            instructions="""
                    Resolve the queries and make sure user is satisfied with the response
                    """,
            chat_ctx=chat_ctx,
        )
        self.ctx = ctx
        self.turn_count = 0

    @function_tool
    async def complete_query(self):
        """Use this to once sure user have no further queries"""
        return self.complete(True)

    async def on_enter(self) -> None:
        chat_ctx = self.chat_ctx.copy()
        chat_ctx.add_message(
                        role="assistant",
                        content=f"""Provide a resolution from below cases else ask user to state the issue.

                        Issue Category
                            - Location Based - Ask User to change location like this - Kripya apna location badal kar phir se rides check kijiye.
                            - Other Issues - Tell User that you have escalated this issue to senior person and they will call you soon"""
                    )
        await self.update_chat_ctx(chat_ctx)
        await self.session.generate_reply(user_input=self.ctx.proc.userdata.get("init_message",""),
                                          instructions="Provide a resolution if the user input has an issue stated else ask user what issue he/she is facing")
