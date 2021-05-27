import requests,os,shutil
import tabula

def get_textual_data_from_pdf():
    # pdf_table = read_pdf('downloads/russell_3000_list/ru3000_membershiplist_20200629.pdf',
    #               output_format='csv',pages='all')

    tabula.convert_into("downloads/russell_3000_list/ru3000_membershiplist_20200629.pdf",
                        "downloads/russell_3000_list/russell_3000_list.csv",
                        output_format="csv",
                        pages='all')

    #  Opening file for reading
    f = open('downloads/russell_3000_list/russell_3000_list.csv','r')

    for val in f.readlines():
        #  Creating list with company name and ticker in it.
        company_data = val.split(',')
        if 'Company' not in company_data:
            #  Removing spaces
            company_data = [company_ticker for company_ticker in company_data if company_ticker != ""]
            #  Printing everything but newline character at the end.
            print(company_data[:-1])


def create_download_directory(directory):
    #  Creating directory if it doesn't exist. If it does exist
    #  remove it and add it again.
    try:
        #  Making directory
        os.mkdir(directory)
        return
    except:
        #  Delete directory if it existed...
        try:
            #  Removing path
            shutil.rmtree(directory)
        except:
            #  This except path means download never existed.
            pass

    #  Creating data directory
    os.mkdir(directory)


def download_data(url, source):
    '''args: url - url where data is downloaded from'''

    print('in download_data function')

    #  Running request to get the needed file.
    r = requests.get(url)

    #  Creating needed variables based on variables sent in.
    url_sections = url.split('/')

    #  Grabbing the filename from the url.
    filename = url_sections[-1]

    #  Creating the download path.
    download_path = 'downloads/' + source + '/' + filename

    #  Creating the extract path.
    extract_path = 'downloads/' + source

    print('Downloading file....')

    #  Creating download directory
    create_download_directory(extract_path)

    #  Writting contents in request to download path.
    with open(download_path, 'wb') as f:
        f.write(r.content)

def main():

    input_bool = False

    while not input_bool:
        user_input = input(
            "Would you like to import the Russell300 list into the database (YES/NO): ")
        if user_input == 'YES':
            print('about to run some stuff')
            input_bool = True
        elif user_input == 'NO':
            print('Exiting...')
            exit(1)
        else:
            pass

    #  Download data
    download_data('https://content.ftserussell.com/sites/default/files/ru3000_membershiplist_20200629.pdf',
                  'russell_3000_list')

    # Reach out russell3000 website download the csv
    get_textual_data_from_pdf()

if __name__ == "__main__":
    main()