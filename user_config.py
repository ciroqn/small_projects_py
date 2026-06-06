def add_setting(settings, setting_item):
    # convert tuple into list of lowercase
    new_setting = [x.lower() if isinstance(x, str) else x for x in setting_item]
    
    # check if key in settings dict. if so
    # don't add, otherwise add - same as other functions below
    if new_setting[0] in settings:
        return f'Setting \'{new_setting[0]}\' already exists! Cannot add a new setting with this name.'
    else:
        settings[new_setting[0]] = new_setting[1]
        return f'Setting \'{new_setting[0]}\' added with value \'{new_setting[1]}\' successfully!'

def update_setting(settings, updated_setting):
    updated_setting_lower = [x.lower() if isinstance(x, str) else x for x in updated_setting]
    if updated_setting_lower[0] in settings:
        settings[updated_setting_lower[0]] = updated_setting_lower[1]
        return f'Setting \'{updated_setting_lower[0]}\' updated to \'{updated_setting_lower[1]}\' successfully!'
    else:
        return f'Setting \'{updated_setting_lower[0]}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(settings, d_setting):
    deleted_setting_lower = d_setting.lower()

    if deleted_setting_lower in settings:
        settings.pop(deleted_setting_lower)
        return f'Setting \'{deleted_setting_lower}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(dictionary):
    if not dictionary:
        return 'No settings available.'

    return 'Current User Settings:\n' + '\n'.join(
        f'{key.title()}: {value}'
        for key, value in dictionary.items()
    ) + '\n'
        
# test dict
test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': False,
    'standby_mode': True
}


