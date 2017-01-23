from google.cloud import datastore
import datetime

def create_client(project_id):
    return datastore.Client(project_id)


def add_task(client, description):
    key = client.key('Task')

    task = datastore.Entity(
        key, exclude_from_indexes=['description'])

    task.update({
        'created': datetime.datetime.utcnow(),
        'description': description,
        'done': False
    })

    client.put(task)

    return task.key

myclient = create_client("steam-sequencer-156512")

mytask = add_task(myclient, input("task description"))

print(mytask)


