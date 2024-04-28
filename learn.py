import uuid

timestamp_uuid = uuid.uuid1()
print("Timestamp UUID:", timestamp_uuid)

namespace = uuid.UUID('{00000000-0000-0000-0000-000000000000}')
name = 'example'
uuid3 = uuid.uuid3(namespace, name)
print("uuid3():", uuid3)

random_uuid = uuid.uuid4()
print("Random UUID:", random_uuid)

uuid5 = uuid.uuid5(namespace, name)
print("uuid5():", uuid5)
