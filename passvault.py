import PySimpleGUI as sg
from sqlitedict import SqliteDict
import string
from random import *
import pyperclip

##### Current Features #####
# Create 1 account
# Search for username and password by typing in webiste name
# Automatically copies the searched password to clipboard
# Delete Account
# Add information
# Edit information
# Generate strong unique passwords
# If you create a new account old one gets deleted (Safety Feature)

##### WIP Features ######
# List entire list
# Delete a websites info from account

def delete_vault(cache_file='cache.sqlite3'):
    with SqliteDict(cache_file) as mydict:
        mydict.clear()

def add_user(key, value, cache_file='cache.sqlite3'):
    try:
      with SqliteDict(cache_file) as mydict:
           mydict[key] = value
           mydict.commit()
    except Exception:
        return

def save(key, value, cache_file='cache.sqlite3'):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value
            mydict.commit()
    except Exception:
        return

def load(key, cache_file='cache.sqlite3'):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key]
        return value
    except Exception:
        return
        
def pass_vault(website, username):
    letters = string.ascii_letters 
    digits = string.digits 
    symbols = string.punctuation
    chars = letters + digits + symbols
    min_length = 8
    max_length = 15
    password = "".join(choice(chars) for x in range(randint(min_length, max_length)))
    user_pass = [username, password]
    save(website.lower(), user_pass)

gplv3 = """
    PassVault, Is a simple to use password manager
    Copyright (C) 2021  Johnny A. Scott Jr.

    This program is free software: you can redistribute 
    it and/or modify it under the terms of the 
    GNU General Public License as published by
    the Free Software Foundation, either version 3 of 
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will 
    be useful, but WITHOUT ANY WARRANTY; 
    without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
    See the GNU General Public License for more details.

    You should have received a copy of the GNU 
    General Public License along with this program.  
    If not, see https://www.gnu.org/licenses/gpl-3.0.txt"""

about = """
    PassVault Copyright (C) 2021 Johnny A. Scott Jr.
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute 
    it under certain conditions"""
    
lock_icon = b'iVBORw0KGgoAAAANSUhEUgAAAW4AAAH/CAYAAAB3mDdpAAAWU0lEQVR42u3da5XjuBYG0CAIBEMIBEMIhEAIhFAIBEMIBEMIBEMIBN/ylGtuTdej85BsPfZeK3/u3NVdZR99rRzJ8mYDAPCqcRy3b592/pzmz/nt03/63MbX3f74M8+f/r6Pv3/rjgD8N5yPc1BOwXkd03Wdf8bT/DMLdaDokN69fQ6fAvo2luP2KdCn33HnjgO5zqRLDOlnwtzMHEgyrPdzf/g68lurZbpGexUDrBHUzdzn7eXx0/r5GjYqCogV1rt5xjjI3OCG+drqjwPCWogDtbRBhHVaIa6dAnwJ6+28lc3iYtqLmwc7VEBgT62QrtItezlvNey0UqC+wDa7LmgWrqKh7HbIyey62Fn4SRsFygnsRjukujaKxUzIPLCpkwAHgY0ABwQ2AhwqDeyPRUe4h0VMWDm0jxYdeXIR82gEwbKBPZ3xPMgfXjTVUGtEQfw+di9vCKzX/4Y4oa2PTfT+t5EG2iJon0BVgT3tFjnLEVZytvsEzLIx+wazbDD7hnVDezob21GrpGqqTWeAw6fQPsoFMuHBHbRGRvuyyU+vdULNC5AeVydXNwuXaI2A1gkk2xrpjHUK02mdUGpoN6NdI5Rrqm3nnVBUaO/0s6mk723LIEWE9sF4pjIHI5+cQ9uJftTKSYNkGdoWIal+0VISkEtge6gG/m8aC3ackHxo2zkC/3UV3ghtEN7wcmjbow3Cm4xC2x5tuJ+93ghtEN4gtEF4U+xC5GDswUsGPW/sHoH8WLBEaIPwBqENwptsg7sztiAqZ5sgtEF4U2toez8kLMt7LHkptL0EAdaxl0A8E9oesIH1eECHp3aQDMYOrGoag3aacHdw2/aX5wyt/8vHN6j89BKJe0L7bKykN3jH9509p3ndoZ0+Ae51O38O85/djd5elKKzZMJiZNpfjS9ziE6B2qxYC838M5zmn0nrbF3eHI/FyISCupv/wWwyqJFm/lk7Qb5KK8xiJV8WI/W1lzHNXo85BPWdQX6cfyfi81g8/xmAnTERPawPJQ+6+R//gxCPzpOV/DPg9sZCtNlR0WF9R4j7FheHh3MqD+1GXzt4H7LTi/yydtKps+B11qiuegdVbwwEW2Q86j/+dRZ+tKgZjP3dlQ4kh0eFCWzbtB6vvYMAD8JhVFokCGwBrmWCFonARoBrmaBFsuLM5qR6otfmyTdBLRO0SELoLDouWqPb0XMFWib8Z1B4OOJ+0x7kVtWsVqvtaB/4Iy6qpsyB4EGb+2mLpNU+4T4ezCnw66fFn/tm2R6eSa9+d2bfdy+ea+uZtZhlo47VMWsUe6OW/7qwo5edV+/bAvvvLFQWUOgWJH/W+2qZbeuvV74WKkuenfA9r4PKv769Zu9nvkVmXNgWdL5vjXj6sZwaP2idfP9tUnXkW9B8DW27Rsqrda/d+54JSobFbPvf161+Fm3KrffGN8yv2wNVhtl27qFtEbL8uvfuVLNus22hjfA268Zse2lerFrvOOiUv1m32bbQRnibdWO2LbRZYEx4AM2s22xbTxs9b7NuzLaFNsLbrLva4qy9MAehzV/Cu/ZvpFeVkFZR1n4miSciuWeceMLSGSZJFeRFMYJJzh2cHJhIIdZ+3ra+HY+OmdrXgxz9kEAR1ny0pW1/PDtuuorHjSONEyjAWnt2dpDwyripeafJTQX4yrfWYqSve4RoM9Y68dFiXLHwekUHJj9P8KKFFWcLVsXh9bFU664s31pXKLYaFyUHfW0i9bsHi5QsUWw1Fpr92sQaTzXu73Z+iSKz9Y/sx1VnMoQCC7uLRIuEJVomNxMiYhVYbcVlFwlLja3adpnY071QYe1tW4KoY6y2bbZ7d12bJDSn/rH0GNtpl6BNoqAwQdIuqbiYatpN4rF21hxrtT0Ob3dJxGKq6aGbkzvOyuPtVNF48zBOxEIabP+DxcZbTdsDPYwT8aub2TaYdceiNRmhgI5m22DWHdHRHQ9fQLWcYKbXRmpjr5a1JSdvRiieWv7V93UNbUrbAosonFq2Adq3TapjsJZ93bYFBiyak6IBkycbA/Iqmr6Cgrm60yQ+Dmt4ubCzgfS3H+IEQFIfhzWcHKjPHahYajnwxhZAUh+L20rGooPdAhRLDfu3LUqSy3isYZHSfm6FchfnAZPLeNybSHFPoZS+IKKnRm5jsvQ1JxsFAhSJf93Bt+BFucuvFUgNe0e1SdAu8UxFUQVS+sKkNgm+CdueW1xxlH64jUNtyHVsln7om8PeXiiO3rYj8G14BZ6gfKE4Sl+9dhIguY7N0k8M1MbUR/uWVyWR+/gc7Czhz6IofUeJbYDkPkZL3xZoZ8kTRVH6liOr1uhz26pbXFGUfga3g2zIfYyWfgCcs7l9DdM/o8hxqp3Jfwqi5K2AthphnBqnRRZEyYdL2dxPKeO05IfkHDblK5gHbyhynBa9QOkOC27bjChxnLaCm49iKH212mvKKGWslv46M7u//CvuX3F8O/btWHBbqYb1x2svuJkK4SC4QXAnwBPODxRCyU9N2gpIaeO15C2Bnp4U3AoB49V4VQgKAYxX41UhWOyAB8drK7gp/X12ghvBnQ/vhX2gEGwvAsFtF5jgFtwguAW34BbcILgR3CC4BbfgTk/jDlPYeN0JbooObneXQses4FYEghsEt+AW3IIbBLfgFtyCGwQ3ghsEt+AW3IIbBLfgFtyCGwQ3ghsEt+AW3IIbBLfgFtyCGwQ3ghsEt+AW3IIbBLfgFtyCGwQ3ghsEt+AW3IIbBLfgFtyCGwS34BbcghvBLbgFt+AGwS24BbfgBsEtuAW34EZwC27BLbhBcAtuwS24QXALbsEtuBHcgltwC24Q3IJbcAtuENyCW3ALbgS34BbcghsEt+AW3IIbBLfgFtyCG8EtuAW34AbBLbgFt+AGwS24BbfgBsGN4AbBLbgFt+AGwS24BbfgBsGN4AbBLbgFt+DO4T43b5/27bN/+5zmTzff/4/PsMJtuv7xM3Sffr79/DM37qDgRnCXei+3c9Ad3z7nFcM4lmH+nc7z7zj9rlvBLbgFt+DO6d6188z0UlhAPxPol/latIJbcAtuwZ3SbHo/zzavI/e0YM7zNdsKbsEtuAX3UvdmN88iBXWYIJ+u5U5wC27BLbhD34/9vEA3yNqorZXpGu8Ft+AW3IL71bC+ydTF3XILccGN4F7vujdzD9bMOq2Z+HRPGsEtuAW34P58vQ961nmEyHSvBLfgFtyVBven2bVWSJ6tlFNKs3DBjeCOe23buX9KGaZ7uRPcgltwFxjcc2D3cq7oNkoruAW34C4guAW2ABfcgltwZxLcAluALxngghvB/fqi40VuMZtqoRHcgltwJxjc4/u5IWc5xQ+m2tgKbsEtuBMJ7vH9OFHb+vibqUaOgltwC+4Vg3t8P/DJgzM8aqqZneAW3IJ7weDWFiG19ongRnD/fbfIIHMIZKqlVnALbsEdIbjNskl59i24Edzf97LNslli9r0T3IJbcL8Y3OP7YUKwpJPgFtyC+4ngnlsjvQxhrcB6pHUiuKk+uMf3BUj7slnb7d7WieCm6uAe3x+mgZQcBTeC++fWSCcjSFQnuBHcX0PbE5CkbqrRreCm+uAebfUjL1Ot7gQ31Qb3aBGSPE012wpuqgvu8f3N6pCzg+CmmuAW2pQW3oKbooN79CQkalpwC24AwS24AQS34AYEt+AGENzJhHarVoCEtJL599CeHv32QAqQkimTthJaiwTQMikitB1nCqTsKKm/HrQEkLqdxP5/cDvSFMjBVWJvvAwXyM5JiwRAy0SLBEDLRIsEoO6WiRYJoGWiRQKgZeJBG4C7HEsP7WZ0FglQlrLPMnn75S7uMVCgi+NaAfLTlhjcg/sKFGywIAmQn2Mpoe3lCEAtyliofPslzu4lUJFzCdv/AGrT5BzcvfsHVOiSa2jb/gfUrDXbBshLb7YNYNbt9D+AyK65hPbBvQL418Gj7QB5Gcy2Acy69bYBIrvaSQKQnzbF4O7dF4Af9WbbAGbdXkkGENklldB2AiDA/ZoUgrtzHwDu1nm7DUBe1n1LzuhdkgDPOK4Z3IPrD/CwYa3Q3rv2AE/b2wIIkJeLLYAA+WmWDO6T6w3wspNFSYC8DEuFtnNJAMJplwjuznUGCKaLHdqelAQIK+6TlKNXkwHEcIgZ3L3rCxBcb+82QH6aGMHtQCmAeI4xgtsb3AHiuWqTAOSn0SYByMtRm4QaTHtg+/H9wbDT/Jm2rbbz5/Dpf+/m/69nEUhVH/KhG0gpqLs5kJsX23+H+c8S5KRk66EbSgrrXcRnFHZCnEQcQhR05zqykmGeOCz2YtX5G+ZhdAIm6+lCFLIZCKsE9mZlApy1vmGG+PoIS7ZETpvEjO8LmyYwLGlnGyA56MclX+P03GJm7zaxkOMrxapQSbtIlw9wkxkWmci8UqQQuzXSbjIzvu8P1zohqmeLc+/SEdH0UNduk6nxff3Hg2nEtH+mMM+uGxFDe7vJ3Pi+dVB4E8vZY+4IbeFNZmPFY+6kYCgptP8YL4PbSwTbRxdfIKRpMW+3KdT43vO2YElo7SNFeHK9CGy/KdxoQZ/wTo8UYO96EdB5U4nRoj5h9Y8Un698hDKMBfa19btZyO2RXh2E0m4qM1ojIqzdPUXn/G1C6TaVGh2HTDgHPToW+4o3Jnxo1EKHUmk5EsL5noLrXScCOG0qN9qdRRj9PcUGIWwF9z+zbniZQmMJ3Qa9bkJqPEBAbDuRbZcWQe315IhpENdfxtWgLHjR6bcCu7g+RCswi5QQvv042lGCNol2CSnq7SghlpuYdowEcfx2xgK84iKitSGJZut8BWI4imh9bqJpnVHCMoWFiRGh7M0IWOarHFqRhHLyhBfBiWfHSRBVZysgoXnwxoM4xNUrKuIXFSZHxJ0cuSYIbsFNRu3I0ZNdCG7BTQ4aW5UQ3IKbvLSfC8pxrghuwU1mwW0PN6+6iua/BvdVmfCik+AmKNFsHzeCG8EtuOGX4NZ7I2z/DWeVEEMvuAnN6YA/B/dReSC4SZG3u/8c3J3yIHRwW+0mBOeVOKeEBYMbQmnE9JfQbpQFoQhuYtDn1t9GcJMZD+J48AbBjXaJNgkIbmI7i+x/x9ZZOSC4ycFt9P7Jj/dM3pQDgptcnAS3oyQQ3Jh1m20juC2eYNZtto0ZN/xpV2FoexUggpus9RUGd++2I7jRMtEiAcHN4toKQtuZ2whuijLtsGgKDu1mtIsEwU2BpjM7tgWG9nZ0HgmCG+EttEFwI7yFNoIb6g1voU0KwT24HKxgqrtdhqG9M2ZYa8x4YIAUTDsxDhmF9mG0e4T1eMs7Sbmk3DqZWyMXtwnBDRnMvs2ySTW4zSRIRoLBDanonK+A4Bbc5OUkuBHcgpuMg/voeiC4BTfJOzjVDMEtuMlLK7gR3IKbjIN763oguAU3ydsqTgS34CbnsTE6ewHBLbhJ2eAFpwhuwU1e+u+Ks3NdENyCm2R13k6N4Bbc5OX0XXHuXRcEt+AmWfvvitNebgS34CZdrQJFcAtuShgXozOHEdyCmxTdfivQ3vVBcAtuktP/VqBn1wfBLbhJzvm3AnW8K4JbcJOe428FamcJgltwk55WkSK4BTcljYnRYVMIbsFNSoZ7itQb3xHcgpt0XO4pUmeWILgFN+k43VOkFigR3IKbdLT3FKnXmCG4BTfp2N5bqFfXCsEtuFnd9ZFC7VwvBLfgZnXdI4V6cL0Q3IKb1R0eKdTG9UJwC25W1zxarINrhuAW3KxmeKZYO9cNwS24WU33TLHqcyO4BTfrOTxTrPrcCG7BzXqaZwt2cO0Q3LC44ZWC7Vw/BDcsrnulYPeuH4IbFrd/pWCdW4LghuVtXy3a3jVEcMNi+hBF6wXCCG5YzjFE0doWiOCG5TShCtcxrwhuiO8asnDPrieCG6I7hyzcneuJ4IbodqGLd3BNEdwQzRCjeLVLENyQQ5tEuwTBDRm2SbRLENyQWZvEwzgIbojqGLOAPYyD4IbwmthF3LvGCG4Ipl+iiL3SDMEN4RyWKOLpqNeba43ghpdNWbpdqpA71xvBDS/rlixke7oR3PC63dLF7MRABDc877pGMVukRHDD8w5rFLNFSgQ3PGe5RUkHTyG4IYjzmgXtSUoENzyuWbuoL+4BghvudkmhqFv3AcENd2tTKezevSCgXUKh7ZkFQupTmpHYGkhI+4Rqe+92ENAhta+Tg3tCIF1Cdd25HQQybBLsA5p1U1yBm5BQ7GxbkVNiu0SbhKJn22bdRNAnUM+920DRs22zbiJoV6xj21wpf7Zt1k0E1xXr2OmX1DHbNusmgvMK9esMHuqZbZt1k/uMRe1S5WzbrJtcB4DQptrZtq1U5BjeQpsI9pscjbZTEV43BjyAfnx/IUjnshJYv8nVaEsVkb6Chph9z7PsweUkgnaTM7MZIgf48ZEZ+DzDPgpsYn4r3ORu9JYcljHtuz7Ps+j2j89h/m/2ZrOEZlOCt1/k5F4CFThtSjF/PfXVFCjZlHHbTUlG2wOBsu03JRptDwTK1G9KNVqoBMrUbEo2WqgEynLa1GC0UAmUYdjUYvREJVCGdlOT0ZnHQN7Om9qM9nYDGbdIxtL2bGuZAFokWiYAWiRaJgBaJK+E9049ABnYSWwP5gD5OElqZ5kA+egl9O9nmdzUCJCQKZMaCe34VyAfe8lsiyCQD1v/Hgxv7wcE1nSVxPrdQD70tT0SD2SmlcCvhfdRDQELOkreMOHdqSVgAZ3EDXueicVKIKYpY5xDEiG8LVYCMdyEdtzDqIQ3EDq0HR4VObwP6gwI6CBZ7TQB8mEHiZ0mQEbsIBHegNDGNkEgBtv+hDcgtBHegNCuJLydJgj8xGl/HtABMgttD9gIb0BoI7wBoS28hTcIbYQ3ILQR3oDQ5uetgvZ5Q9mmMW7Ln4d0gIxC28M1whsQ2qQU3p1ahyJ0QruuABfekHloS7I6w9ubdCBP3lxTeXhP77C0XRDyMI1V74jEXm/IKLTt0cZeb8iEPdrYcQIZmcaknSNYtIRMWITkofBu9b1h1X52K4nQ9wb9bCoK8LOxBIs4SxxChvde6wSitkb2kgatE9AagX8D/GSsQRAnicLSu04G4w6eMo0dT0GySnhPD+xYuITHTGPGAzWYfUMms2x7szH7BrNsMPsGs2yqnX3beULt7BghywCf9n33xi+VmWrevmyyD3Bv2aEG3k6D9gnk1Bax+Ejp7ZOLcU4hLtoi1BTgrf43mfex7Rah6v73IAfIxKCPDQIcgQ3ZB/hptAOFdEy1aD823BHeHztQzMBZc4ZtpwhooaAlAvUFuLfvEMtVYEO8ALeNkJCmWrKtDxYK8OlBns5CJk8uOE6148EZWCnAt/rgPNK/tuAI6bVROvnEN7Nr7RDIZBZuMbPyxUaza8i3F25PeD2tkJPeNZQV4rvx/d1/QryssJ7u6U6FgxBHWAOJh/hRTzz5nvVRWAPfhfjHwmZnNr76rLqzwAg8E+TNPNO7jB72ib1t72JWDcRqq5iRh51RC2pg8dZKO29DuwjzH0P6Ml+jVusDSDnMj/Puh76SNstt/l3P8+8upIFiAv0wzz67OeiGzGbP/fyzn+bfRUAD1Qf7x2z99KkF03/63CLMkj8+l09/7/HTzyOYScL/AGTTM9p8uEvXAAAAAElFTkSuQmCCl9Qx2zbrJoLzCvXrDB7qmW2bdZP7jEXtUuVs26ybXAeA0Kba2batVOQY3kKbCPabHI22UxFeNwY8gH58fyFI57ISWL/J1WhLFZG+goaYfc+z7MHlJIJ2kzOzGSIH+PGRGfg8wz4KbGJ+K9zkbvSWHJYx7bs+z7Po9o/PYf5v9mazhGZTgrdf5OReAhU4bUoxfz311RQo2ZRx201JRtsDgbLtNyUabQ8EytRvSjVaqATK1GxKNlqoBMpy2tRgtFAJlGHY1GL0RCVQhnZTk9GZx0DezpvajPZ2Axm3SMbS9mxrmQBaJFomAFokWiYAWiSvhPdOPQAZ2ElsD+YA+ThJameZAPnoJfTvZ5nc1AiQkCmTGgnt+FcgH3vJbIsgkA9b/x4Mb+8HBNZ0lcT63UA+9LU9Eg9kppXAr4X3UQ0BCzpK3jDh3aklYAGdxA17nonFSiCmKWOcQxIhvC1WAjHchHbcw6iENxA6tB0eFTm8D+oMCOgg'

gpl_button = b'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'

sg.LOOK_AND_FEEL_TABLE['PassVaultTheme'] = {'BACKGROUND': 'grey19',
                                         'TEXT': 'ghostwhite',
                                         'INPUT': 'grey60',
                                         'TEXT_INPUT': 'grey1',
                                         'SCROLL': 'grey60',
                                         'BUTTON': ('grey60', 'grey1'),
                                         'PROGRESS': ('grey35', 'grey9'),
                                         'BORDER': 1, 'SLIDER_DEPTH':0,
                                         'PROGRESS_DEPTH': 0, }

def about_window():

    layout = [[sg.Text(about)],
              [sg.Button('', image_data=gpl_button,
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         border_width=0, key='copyright')]]

    window = sg.Window('About', layout, icon=lock_icon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'copyright':
            window.Close()
            license(gplv3)
            welcome_window()
        else:
            break

def you_sure():

    layout = [[sg.Text('Are you sure?')],
              [sg.Button('Yes'), sg.Button('No')],]
              
    window = sg.Window('New Account', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == 'Yes':
            delete_vault()
            window.Close()
            newuser_window()
        elif event == 'No':
            window.Close()
            welcome_window()
        else:
            window.Close()

def my_popup(info):
    
    layout = [[sg.Text(info)],]
    
    window = sg.Window('Info', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

def license(gplv3):
    
    layout = [[sg.Text(gplv3)],]
    
    window = sg.Window('License', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

def welcome_window():

    sg.theme('PassVaultTheme')

    layout = [[sg.Button('Login'), sg.Button('Create Vault'), sg.Button('Delete Account'), sg.Button('About'), sg.Button('Exit')],]
    
    window = sg.Window('Welcome', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
        	break
        if event == 'Login':
            window.Close()
            login_window()
        elif event == 'Delete Account':
            window.Close()
            remove_window()
        elif event == 'Create Vault':
            window.Close()
            you_sure()
        elif event == 'About':
             window.Close()
             about_window()
        else:
            window.Close()
            
def remove_window(cache_file='cache.sqlite3'):

    sg.theme('PassVaultTheme')

    instruct = "Please enter your login username and password"

    layout = [[sg.Text(instruct)],
              [sg.Text('Username:', size=(10,1)), sg.Input(key='log_user')],
              [sg.Text('Password:', size=(10,1)), sg.Input(key='log_pass')],
              [sg.Button('Remove'), sg.Button('Cancel')],]
              
    window = sg.Window('Delete Account', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
        	break
        if event == 'Remove':
            with SqliteDict(cache_file) as mydict:
                user = values['log_user']
                secret = values['log_pass']
                if user in mydict and secret in mydict.values():
                    delete_vault()
                    sg.popup('Account Deleted')
                    window.Close()
                    welcome_window()                  
                else:
                    sg.popup('Wrong login info')
                    window.Close()
                    welcome_window()
        elif event == 'Cancel':
            window.Close()
            welcome_window()
        else:
            window.Close()
            
def login_window(cache_file='cache.sqlite3'):

    sg.theme('PassVaultTheme')

    instruct = "Please enter your login username and password"

    layout = [[sg.Text(instruct)],
              [sg.Text('Username:', size=(10,1)), sg.Input(key='log_user')],
              [sg.Text('Password:', size=(10,1)), sg.Input(key='log_pass')],
              [sg.Button('Submit'), sg.Button('Cancel')],]
              
    window = sg.Window('Login', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
        	break
        if event == 'Submit':
            with SqliteDict(cache_file) as mydict:
                user = values['log_user']
                secret = values['log_pass']
                if user in mydict and secret in mydict.values():
                    window.Close()
                    menu()                    
                else:
                    sg.popup('Wrong login info')
                    return
        elif event == 'Cancel':
            window.Close()
            welcome_window()
        else:
            window.Close()

def newuser_window():
    
    sg.theme('PassVaultTheme')
    
    case = 'Username and Password are both case sensetive'
    
    layout = [[sg.Text(case)],
              [sg.Text('Username:', size=(10,1)), sg.Input(key='new_u')],
              [sg.Text('Password:', size=(10,1)), sg.Input(key='new_p')],
              [sg.Button('Create'), sg.Button('Cancel')],]
              
    window = sg.Window('Create Your Vault', layout, icon=lock_icon)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
        	break        
        if event == 'Create':
            new_u = values['new_u']
            new_p = values['new_p']
            add_user(new_u, new_p)
            sg.popup('Vault Created')
            window.Close()
            welcome_window()
        elif event == 'Cancel':
            window.Close()
            welcome_window()
        else:
            return

def add_window():

    sg.theme('PassVaultTheme')

    layout = [[sg.Text('You will need to put in the following info:')],
              [sg.Text('Website:', size=(10,1)), sg.Input(key='input_web')],
              [sg.Text('Username:', size=(10,1)), sg.Input(key='input_user')],
              [sg.Text('Password:', size=(10,1)), sg.Input(key='input_pass')],
              [sg.Button('Okay'), sg.Button('Generate'), sg.Button('Cancel')],]

    window = sg.Window('New Password Info', layout, icon=lock_icon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
        	break
        if event == 'Okay':
            website = str(values['input_web'])
            username = str(values['input_user'])
            password = str(values['input_pass'])
            user_pass = []
            user_pass.append(username)
            user_pass.append(password)
            save(website, user_pass)
            sg.popup('New Account Added')
            window.Close()
            menu()
        elif event == 'Generate':
            website = str(values['input_web'])
            username = str(values['input_user'])
            pass_vault(website, username)
            sg.popup('New Account Added')
            window.Close()
            menu()
        elif event == 'Cancel':
            window.Close()
            menu()
        else:
            window.Close()

def edit_search():

    sg.theme('PassVaultTheme')

    layout = [[sg.Text('Search for the website you wish to edit')],
              [sg.Text('Website:', size=(10,1)), sg.Input(key='edit')],
              [sg.Button('Search'), sg.Button('Cancel')],]

    window = sg.Window('Edit Search', layout, icon=lock_icon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
        	break
        if event == 'Search':
            web = values['edit']
            window.Close()
            edit_window(web)
        elif event == 'Cancel':
            window.Close()
            menu()
        else:
            window.Close()

def edit_window(web, cache_file='cache.sqlite3'):

    sg.theme('PassVaultTheme')
    
    usr = 'Save Username'
    sp = 'Save Password'
    sb = 'Save Both'
    no = 'Cancel'

    layout = [[sg.Text('Enter your new password')],
              [sg.Text(web)],
              [sg.Text('Username:', size=(10,1)), sg.Input(key='new_user')],
              [sg.Text('Password:', size=(10,1)), sg.Input(key='new_password')],
              [sg.Button(usr), sg.Button(sp), sg.Button(sb), sg.Button(no)],]

    window = sg.Window('Edit', layout, icon=lock_icon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
        	break
        if event == 'Save Username':
            password = load(web)
            e_user = values['new_user']
            old_pass = password[-1]
            edited = [e_user, old_pass]            
            save(web, edited)
            sg.popup('Saved')
            window.Close()
            menu()
        elif event == 'Save Password':
            username = load(web)
            old_user = username[0]
            e_pass = values['new_password']
            edited = [old_user, e_pass]
            save(web, edited)
            sg.popup('Saved')
            window.Close()
            menu()
        elif event == 'Save Both':
            e_user = values['new_user']
            e_pass = values['new_password']            
            edited = [e_user, e_pass]
            save(web, edited)
            sg.popup('Saved')
            window.Close()
            menu()
        elif event == 'Cancel':
            window.Close()
            menu()
        else:
            return
        
def menu(cache_file='cache.sqlite3'):
    sg.theme('PassVaultTheme')

    menu_def = [['&Password', ['&Add','&Edit',]]]

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.Text('Pick website for login info')],
              [sg.Input(key='search_web', size=(30,1))],
              [sg.Button('Search'), sg.Button('Print'), sg.Button('Exit')],]
    
    window = sg.Window('PassVault', layout, grab_anywhere=True, icon=lock_icon)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Search':
            search = str(values['search_web'])
            info = load(search.lower())
            try:
                pyperclip.copy(info[-1])
                my_popup(info)
            except Exception:
                sg.popup('You have no saved information')
        elif event == 'Add':
            window.Close()
            add_window()
        elif event == 'Edit':
            window.Close()
            edit_search()
        else:
            return

welcome_window()
