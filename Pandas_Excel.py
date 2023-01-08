import pandas as pd
import faker

faker = faker.Faker()

df = pd.read_excel('fake_data.xlsx')

df.head(8)

adrs = []
for i in range(20):
    adrs.append(faker.address())
    
print(adrs)

df.insert(3,'Address', adrs)

df.head()

df.to_excel('fake_data.xlsx', index=False,sheet_name='Test')
