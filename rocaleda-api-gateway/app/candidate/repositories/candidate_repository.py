import httpx


class CandidateRepository:
    async def get_candidates(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/users")
            return response.json()
