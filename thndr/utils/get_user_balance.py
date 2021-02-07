def get_user_balance(user_id):
    from thndr.models import Transaction
    balance = 0
    wallet_tx = Transaction.objects.filter(user__pk=user_id, is_wallet=True, is_stock=False)
    for tx in wallet_tx:
        balance += tx.amount
    return balance
