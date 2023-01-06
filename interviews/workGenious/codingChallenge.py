class Account:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0
        self.transfer = 0


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, timestamp, account_id):
        if account_id in self.accounts:
            return False

        self.accounts[account_id] = Account(account_id)
        return True

    def deposit(self, timestamp, account_id, amount):
        if account_id not in self.accounts:
            return ""

        account = self.accounts[account_id]
        account.balance += amount
        return account.balance

    def transfer(self, timestamp, source_account_id, target_account_id, amount):
        source = self.accounts.get(source_account_id)
        target = self.accounts.get(target_account_id)

        if not source or not target:
            return ""

        if source == target:
            return ""

        new_source_balance = source.balance - amount

        if new_source_balance < 0:
            return ""

        source.balance = new_source_balance
        target.balance += amount

        source.transfer += amount

        return new_source_balance

    def top_senders(self, timestamp, top):
        accounts_dict = {}
        response = []

        for account in self.accounts:

            acc = self.accounts[account]

            if acc.transfer in accounts_dict:
                accounts_dict[acc.transfer].append(account)
                continue

            accounts_dict[acc.transfer] = [account]

        for transfer in dict(reversed(sorted(accounts_dict.items()))):
            sorted_items = sorted(accounts_dict[transfer])

            while len(sorted_items):
                response.append(f"{sorted_items.pop(0)}({transfer})")

        return ", ".join(response[:top])


def solution(queries):
    bank = Bank()
    responses = []

    for query in queries:

        action = query[0]
        timestamp = query[1]

        if action == "CREATE_ACCOUNT":
            account_id = query[2]
            res = bank.create_account(timestamp, account_id)

            responses.append(str(res).lower())

        elif action == "DEPOSIT":
            account_id = query[2]
            amount = int(query[3])
            res = bank.deposit(timestamp, account_id, amount)
            responses.append(str(res).lower())

        elif action == "TRANSFER":
            source_account_id = query[2]
            target_account_id = query[3]
            amount = int(query[4])

            res = bank.transfer(timestamp, source_account_id, target_account_id, amount)
            responses.append(str(res).lower())

        elif action == "TOP_SPENDERS":
            top = int(query[2])
            res = bank.top_senders(timestamp, top)
            responses.append(res)

        elif action == "SCHEDULE_PAYMENT":
            pass

        elif action == "CANCEL_PAYMENT":
            pass

    return responses


queries = [
    ["CREATE_ACCOUNT", "1", "account3"],
    ["CREATE_ACCOUNT", "2", "account2"],
    ["CREATE_ACCOUNT", "3", "account1"],
    ["DEPOSIT", "4", "account1", "2000"],
    ["DEPOSIT", "5", "account2", "3000"],
    ["DEPOSIT", "6", "account3", "4000"],
    ["TOP_SPENDERS", "7", "3"],
    ["TRANSFER", "8", "account2", "account3", "1000"],
    ["TRANSFER", "9", "account1", "account3", "1000"],
    ["TRANSFER", "10", "account3", "account2", "2500"],
    ["TOP_SPENDERS", "11", "3"],
]

print(solution(queries))
