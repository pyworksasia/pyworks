from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/profile")
async def profile():
    response = {
        "id": 1,
        "full_name": "John Smith"
    }
    return response


@router.post("/login")
async def login():
    response = {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxOTMiLCJqdGkiOiI1MmI4MzM4MmVlYmI4ODA4MjNkYTEzNjczOWQxYzgzY2YxNWY4ZTE2MmU3YmMyYjhkODVlMWJiOTQwM2Q5ODg2YTZiZjcwZGU4NjI1NDNmMSIsImlhdCI6MTYxNDc4ODQ2NSwibmJmIjoxNjE0Nzg4NDY1LCJleHAiOjE2NDYzMjQ0NjUsInN1YiI6IjExIiwic2NvcGVzIjpbXX0.Y4OyKQIYpBDA8KFuY_ejLu4CVVq2FzJv8eODM9eX6uYL-nxSaOoSMS1339QVw8PBvt8wRe9PppxnQveP9KHggGTcAMY5beMrPkfnVBp4Vvf3DkGrwtCD4jyYkI7ZomFnU9iZhw7hP3FyZ3Cogni52KU-WBL8x7qfknf9zYlDIAVFG2YU5REutT_iiNXHq9Dkaj-3j43o8obijs62yj5c3XdMTJzmJQjj--pssL2lCtRvAQ2KMvKPINieuC4ecliaHB9G0Rc4kk-185SOQofnxpGt-oqdiIHYc3zypukD7Hpr36NYFso80O-P9wa9rwrUSWXpmz-oZ7DMYJPR83-QQHhzpsZcb87bTUpuoFVjF6GJ32Sk7w0ZkbBbYKR6SdoKcF1v9-6zp2OuNSU06KpBErc4RTp2DCcIFUjvlJiGCbSOirDQKQyKcrzBmyys5Hh_2qADlBrcVd5xZ8kd_J06cJFnyb2vxH_FAz7VQT2mX2O_R_x_9F7V5i_ipMY-sS1f-SQAor-ko-lb5bquR4Lr0Trxng6sE_cI_XCy5OuApY0AFz_JH49-piotr_ADMUs5OPBr-aOda9MHG7d0v9zbmudZa_WQ-vf3ywsQ_yqpn96dFFc4aCRN-PGoen8rvbaRfZZlltumhGK15ltoYeY6SDsbUxZnS_aL07mU8o-kQZU"
    }
    return response


@router.get("/logout")
async def logout():
    response = {"message": "Logout successfully"}
    return response
