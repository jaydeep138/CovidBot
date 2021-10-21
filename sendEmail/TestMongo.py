from pymongo import MongoClient
client = MongoClient("mongodb+srv://covidBot:ja49u8F.*2N8FTv@cluster0.4vevt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('covid19DB')
records = db.chat_records
print(records.count_documents({}))
new_chat = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}


records.remove()


