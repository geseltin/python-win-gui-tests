from model.group import Group
import random



def test_delete_group(app):

    old_list = app.group.get_group_list()
    if len(old_list) == 1:
        group = Group()
        app.group.add_new(group.name)
        old_list.append(group.name)

    group_to_delete = random.choice(old_list)
    app.group.delete_by_name(group_to_delete)

    new_list = app.group.get_group_list()
    old_list.remove(group_to_delete)
    assert sorted(old_list) == sorted(new_list)