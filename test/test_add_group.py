from model.group import Group


def test_add_group(app):
    group = Group()
    old_list = app.group.get_group_list()
    app.group.add_new(group.name)
    new_list = app.group.get_group_list()
    old_list.append(group.name)
    assert sorted(old_list) == sorted(new_list)