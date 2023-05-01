from api.core.api_core import BaseApi


class Members(BaseApi):

    def get_members(self) -> dict:
        return self.get('/members')

    def get_member_by_id(self, member_id: str, expected_status_code=200) -> dict:
        return self.get(f'/member/{member_id}', expected_status_code=expected_status_code)
