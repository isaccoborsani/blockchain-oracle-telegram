import requests
import json
import re
import utils


def listtransactionspost(address):
    with requests.session() as s:
        data = {'address': address}
        r = s.post("https://dev.takamaka.io/api/V2/testapi/listtransactions", data=data)
    result = ""
    if r.text != "":
        result = json.loads(r.text)
    return result


def main():
    from_address = ['sZh2gyX7qDu8mAQBWDvDyij6zL1VSHr2-k8nFAP7AB8.', '7COyhKDyouXbtvi48jxFwC7pMG3eXqrW7Al4hjFab0w.',
                    'Msun9pWhL4MeyEgz-DegzqQWOT5Z-TE1WxSqy2YFZ5I.', 'F0fkjEOlW8NjNEmfa3djX6LKAiJizp2N5gMuNN5Jl3A.']

    siths = utils.load_resource("siths.txt")

    for single_from in from_address:
        trx_list = listtransactionspost(single_from)

        telegram_users_to_be_processed = {}

        for single_trx in trx_list:

            upper_dict = {}

            for key, val in single_trx.items():
                upper_dict[key.upper()] = val

            if upper_dict['SITH'] not in siths and 'MESSAGE' in upper_dict and upper_dict['MESSAGE'] != '':

                trx_type = 'charge'
                if 'upload_file_trx' in upper_dict['MESSAGE']:
                    trx_type = 'file'

                if re.search('telegram_user_id=\d{1,}', upper_dict['MESSAGE']) is None:
                    continue

                key_to_be_fetched = 'MESSAGE'
                msg_suffix = "Thank you @{} for your interest in Takamaka Blockchain, your file has been \n" \
                             "signed and you can download the certificate by clicking on this link: https://dev.takamaka.io/api/V2/app/testFiles/telegramFiles/{}.zip\n" \
                             "you can also check the transaction here: https://testexplorer.takamaka.dev/searchtransaction/{} "
                if trx_type == 'charge':
                    msg_suffix = "Thank you @{} for your interest in Takamaka Blockchain, check your balance ;-)You " \
                                 "can consult the transaction on our Explorer: " \
                                 "https://testexplorer.takamaka.dev/searchtransaction/{} "

                if trx_type == 'charge':
                    telegram_users_to_be_processed[
                        upper_dict[key_to_be_fetched].split("telegram_user_id=")[1].split("telegram_user_name=")[
                            0]+'_'+str(upper_dict['SITH'])] = msg_suffix.format(upper_dict[key_to_be_fetched].split("telegram_user_name=")[1],
                                                    upper_dict['SITH'])
                else:
                    telegram_users_to_be_processed[
                        upper_dict[key_to_be_fetched].split("telegram_user_id=")[1].split("telegram_user_name=")[0]+'_'+str(upper_dict['SITH'])] = \
                        msg_suffix.format(
                            upper_dict[key_to_be_fetched].split("telegram_user_name=")[1],
                            utils.convert_from_b64_url_to_hex(upper_dict['SITH']),
                            upper_dict['SITH']
                        )
                siths.append(upper_dict['SITH'])
                utils.update_resource(siths, 'siths.txt')

        print(telegram_users_to_be_processed)
        if len(telegram_users_to_be_processed.items()) > 0:
            for telegram_reply_to_id, msg in telegram_users_to_be_processed.items():
                url = 'https://api.telegram.org/bot{}/sendMessage'.format(utils.telegram_token)
                data = {'chat_id': telegram_reply_to_id, 'text': utils.clean_string(msg)}
                requests.post(url, data).json()


if __name__ == "__main__":
    main()
