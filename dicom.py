from pynetdicom3 import AE
from pydicom.dataset import Dataset
from pynetdicom3 import QueryRetrieveSOPClassList

ae = AE(scu_sop_class = QueryRetrieveSOPClassList)

ip = "IP ADDRESS HERE"
port = 104
association = ae.associate(ip, port)

if association.is_established:
	print('[+] Association established!')

	dataset = Dataset()
	dataset.PatientName = '*'
	dataset.PatientID = ''
	dataset.PatientSex = ''
	dataset.PatientBirthDate = ''
	dataset.StudyDescription = ''
	dataset.QueryRetrieveLevel = "PATIENT"

	results = association.send_c_find(dataset, query_model='P')

	for (status, dataset) in results:
		if status.status_type == 'Pending':
			print(dataset)
			print('')

	association.release()
