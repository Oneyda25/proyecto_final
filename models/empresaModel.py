from config.database import db

def insertCompany(name, description, image, phone, address, email, password):
    cursor= db.cursor()
    cursor.execute("INSERT INTO users (name, description, image, phone, address, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, description, image, phone, address, email, password,))
    cursor.close()