from tests import BaseTest
from api.member import Members


class TestMembers(BaseTest):
    members = Members()

    def test_get_all_members(self):
        members = self.members.get_members()

        assert members['status'] == 'success', f'The received in the body status is not "success": {members["status"]}'
        assert members['data']['members'], f'No member were returned in the response: {members}'
        self.validate_member_object(members['data']['members'][0])

    # failed as probation_period is not integer in response. We suppose that GET members response is the correct one.
    def test_get_specific_member(self, member_data):
        member = self.members.get_member_by_id(member_data['ID'])

        assert member['status'] == 'success', f'The received in the body status is not "success": {member["status"]}'
        self.validate_member_object(member['data'])
        assert member['data'] == member_data

    def test_try_to_get_not_existing_member(self, member_data):
        member = self.members.get_member_by_id('025a626c4c1c', 404)
        assert 'Mock not found!' in member, f'Unexpected error message: {member}'
