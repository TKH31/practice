from google.cloud import datastore


def create_client(project_id):
	return datastore.Client(project_id)


def list_tasks(client):
	query= client.query(kind="Task")
	query.order = ["created"]

	return list(query.fetch())

myclient = create_client("steam-sequencer-156512")
print list_tasks(myclient)


