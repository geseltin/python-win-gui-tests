from model.group import Group
from generator.groups import GroupData
import pytest


test_data = GroupData().read_group_data_from_excel()



@pytest.mark.parametrize("group", test_data)
def test_add_group(app, group):
    group = Group()
    old_list = app.group.get_group_list()
    app.group.add_new(group.name)
    new_list = app.group.get_group_list()
    old_list.append(group.name)
    assert sorted(old_list) == sorted(new_list)