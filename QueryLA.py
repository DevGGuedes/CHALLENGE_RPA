#

import Utilities as DAO

def searchLA(text):
    try:
        DAO.createDriverChrome()

    except Exception as e:
        print(f'Erro no Sistema {e}')