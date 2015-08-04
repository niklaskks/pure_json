
import os


def setup(file_name, auth_token, content_project_id):
    """
    Checks to see if we can proceed:
     - file present and readable
     - auth_token set
     - content_project_id set
    """

    file_path = os.path.join(os.path.dirname(__file__), file_name)
    assert os.path.isfile(file_path), 'File `{}` is not readable.'.format(file_path)

    assert len(auth_token) == 40, '`auth_token` is too short.'

    assert isinstance(content_project_id, int), '`content_project_id` is not an integer.'
