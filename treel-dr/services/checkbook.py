"""

Authorization: YOUR_SANDBOX_API_KEY:YOUR_SANDBOX_SECRET_KEY
69404e2e99bb329154264ad92b9647c4:f021d824d27854503cfd1d0906ddbccd

sandbox_url = "https://api.sandbox.checkbook.io/v3/"
https://api.sandbox.checkbook.io/v3/check

https://demo.checkbook.io/v3/invoice

Onboarding:
curl --request POST \
  --url https://demo.checkbook.io/v3/user \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"user_id":"james.bond@mi6.com","name":"James Bond"}'


You'll add their info info by calling PUT /v3/user. We will need a
first/last name, business name, address, tax id, and last 4 of
their SSN


name: Moritz Stephan
user_id: moritzst@stanford.edu
publishable_key: becd6a85575046a7922a3d4200fb3072
secret_key: agpWtxfjhZhewmKUiduqIzRe0cYjms


name: Moritz Stephan
user_id: moritz.stephan@outlook.com
publishable_key: 5f624e829a174fac921f281d94a8c2ad
secret_key: egOtdUoUTrDe1XCHYYvv3UoU0LZIlr

name: Santiago Hernandez
user_id: santiaghini@outlook.com
publishable_key: 43d4e38e3de24200bb65704807f1a275
secret_key: zqaBMiJ5T66wkRh1scoTRwAmeesMWb

name: NonProfit 1
user_id: nonprofit1
publishable_key: 07494ece684741bd97a3e7d6525ab6c2
secret_key: SGEnma53frL71rY3GLeu1IXqRMrD5z

name: NonProfit 2
user_id: nonprofit2
publishable_key: 8e8829159e9440a78414172936f34d50
secret_key: RtQrP3RWkIJxscP6w7FZOJqqszPzPk


name: NonProfit 3
user_id: nonprofit3
publishable_key: 2114394b23b94b2c85b8a4839dead713
secret_key: vQaOdBIhnctm41nOT990eLXHfQBnhZ

name: TreeLDR
user_id: treeldr@outlook.com
publishable_key: cd6277fc5c0d406da05acf767926a3ac
secret_key: fOtmYVoXZxqs2l3GkzrKovjcpug1AH

Send between users
curl --request POST \
  --url https://demo.checkbook.io/v3/check/digital \
  --header 'accept: application/json' \
  --header 'authorization: 08ba7e85f2f943499fd0c2593f4db390:NZqufszJ9PO6FdGBgpJ1JR80lUD2i8' \
  --header 'content-type: application/json' \
  --data '{"recipient":"james.bond@mi6.com","name":"James Bond","amount":500000,"description":"Casino Royale"}'


"""
@app.route("/donate", methods=["POST"])
def donate():
    default_nonprofit = 'nonprofit2'
    default_user_email = 'moritz.stephan@outlook.com'
    user_service = dependencies['user_service']

    email = request.form['email']
    nonprofit = request.form['nonprofit']
    routing_num = request.form.get('routing_num', '')
    account_num = request.form.get('account_num', '')
    amount = request.form.get('amount', 25)
    message = request.form.get('message', '')

    try:
        # nonprofit exists
        nonprofit = user_service.getUser(nonprofit)
    except Exception as e:
        # nonprofit doesnt exist -> use default
        nonprofit = user_service.getUser(default_nonprofit)

    try:
        # user exists
        user = user_service.getUser(email)
    except Exception as e:
        # user doesnt exist -> use default
        user = user_service.getUser(default_user_email)

    auth = user.cb_p_key + ':' + user.cb_s_key
    headers = { "authorization": auth }
    data = {
        "recipient": nonprofit.email,
        "name": nonprofit.first,
        "amount": amount,
        "description": f"Donation from {user.first} {user.last} via TreeLDR - {message if message else 'thanks'}"
    }
    requests.post(CHECKBOOK_CHECK_ENPOINT, headers=headers, data=data)


    return redirect(auth_uri)