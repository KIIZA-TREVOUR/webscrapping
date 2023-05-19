import main

# Read the company names from a text file
with open('companies.txt', 'r') as f:
    company_names = f.readlines()

for company_name in company_names:
    result = main.google_search(company_name)
    # link = 'https://twitter.com/amazon'
    twitter_link = main.get_twitter_profile_link(result)
    # twitter_link = 'https://twitter.com/amazon'
    # twitter_handle = main.get_twitter_handle(link)
    # email = main.email_search(company_link)
    print(twitter_link)

    # print(twitter_link)
    # print(twitter_handle)
    # handles = ['@handle1', '@handle2', '@handle3']
    # main.write_handles('handles.txt',twitter_handle)
    
