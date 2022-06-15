import re


# b = "55.0"

# if "小写" in b:
#     a = re.findall(r'\d+', b)
#     e = re.findall(r'.\d+', b)
#     a = a[-1] + b[-1]
# else:
#     a = re.findall(r'\d+', b)
#     e = re.findall(r'.\d+', b)
#     a = a[0] + '.' + b[-1]

# print(a)
# if a:
#     print(1111)
# else:
#     print(2222)

# c = str(a[-1] / 10000)
# print(c)

# b1 = '123345.000'
# if b1.isdigit():
#     print(int(b1))
# else:
#     print(float(b1) / 10000)

# a = 123345.1
# print(type(a))
# a1 = str(a)
# a2 = re.search(r'\d+(\.\d+)?', a1)
# print(a2.group())
# if a2:
#     print(a2.group())
#     print(1111)
#     if a2.group().isdigit():
#         a3 = a1.replace(a2.group(), str(int(a2.group()) / 10000))
#     else:
#         a4 = float(a2.group())
#         print(222, a2.group(), a4)
#         a3 = a1.replace(a2.group(), str(a4 / 10000))
#     if isinstance(a, str) and '万元' not in a1 and '元' in a1:
#         print(77777)
#         a3 = a3.replace('元', '万元')
#     elif isinstance(a, int) or isinstance(a, float):
#         print(88888888888888, a3, type(a3))
#         if a3.isdigit():
#             a3 = int(a3)
#         else:
#             a3 = float(a3)

# print(a3, type(a3))


# d = 111
# if isinstance(d, int):
#     print(1211, d / 10000)
# elif isinstance(d, float):
#     print(2222, d / 10000)



# for i in a:
#     if i == 77:
#         print('True')


# a = '4123345'
# print(type(a))
# a3 = 0
# a1 = str(a)
# a2 = re.search(r'^\d+(\.\d+)$', a1)
# if a1.isdigit():
#     print('intint-int')
#     a3 = int(a1) /10000
# if a2:
#     print(111)
#     a3 = float(a1) /10000
# else:
#     print(222)


# print(a3)

# a = False

# if a is False:
#     print(11111)





f = {
	"program": false,
	"contract": true,
	"project_name": "979797",
	"system_scale": "1\n2\n3",
	"plan_end_date": "2020-12-11",
	"program_count": 1,
	"project_class": "APP检测",
	"report_retest": true,
	"retest_record": true,
	"contact_method": "2",
	"contract_count": 1,
	"project_source": "第三方委托",
	"contract_review": true,
	"field_test_form": true,
	"project_manager": 7,
	"project_members": [4, 6, 5, 7, 16, 17],
	"supervisor_unit": "1",
	"application_book": true,
	"penetration_test": true,
	"document_handover": true,
	"verification_test": true,
	"report_retest_count": 1,
	"retest_record_count": 1,
	"contract_review_count": 1,
	"field_test_form_count": 1,
	"application_book_count": 6,
	"penetration_test_count": 4,
	"supervisor_unit_member": "11",
	"document_handover_count": 6,
	"pretest_equip_recording": true,
	"verification_test_count": 1,
	"confidentiality_agreement": true,
	"document_transfer_archive": false,
	"system_evaluation_process": true,
	"project_implementation_plan": true,
	"source_code_security_review": false,
	"pretest_equip_recording_count": 1,
	"confidentiality_agreement_count": 1,
	"document_transfer_archive_count": 1,
	"system_evaluation_process_count": 1,
	"project_implementation_plan_count": 1,
	"source_code_security_review_count": 1,
	"system_operation_record_retest_test": false,
	"system_operation_record_initial_test": true,
	"system_operation_record_retest_test_count": 1,
	"system_operation_record_initial_test_count": 1
}