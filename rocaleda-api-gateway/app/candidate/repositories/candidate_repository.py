import os

from fastapi import Request

import httpx


class CandidateRepository:
    def __init__(self):
        self.candidates_host = os.getenv("CANDIDATES_MS")

    async def get_candidates(self, request: Request):
        async with httpx.AsyncClient() as client:
            try:
                query_string = "&".join(
                    f"{key}={value}"
                    for key, values in request.query_params.multi_items()
                    for value in values
                )
                response = await client.get(
                    f"http://{self.candidates_host}/candidate?{query_string}",
                )
                return response.json()

            except Exception as exc:
                print(f"Exception type: {type(exc)}")
                print(f"Exception arguments: {exc.args}")
                print("Exception traceback:", exc.__traceback__)

