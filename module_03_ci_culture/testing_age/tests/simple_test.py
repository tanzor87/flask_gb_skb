from module_03_ci_culture.testing_age.social_age import get_social_status


def check_if_can_get_child_status():
    age = 8
    expect_res = 'ребенок'
    function_res = get_social_status(age)
    assert  expect_res == function_res, 'Not matched'


def check_if_can_get_adult_status():
    age = 33
    expect_res = 'взрослый'
    function_res = get_social_status(age)
    assert  expect_res == function_res, 'Not matched'


if __name__ == '__main__':
    check_if_can_get_child_status()
    check_if_can_get_adult_status()