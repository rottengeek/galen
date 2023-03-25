from galen.spider.cookies import format_cookies


def test_cookies():
    cookies = 'aliyungf_tc=AQAAAOgxCHX0LwkAkKfqerDgQpnJBr44; csrfToken=LrCpyhAqhvA9d-R2PKLn84TG; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1543246590'
    print(format_cookies(cookies))


if __name__ == '__main__':
    test_cookies()
