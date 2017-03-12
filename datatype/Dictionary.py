# 딕셔너리 자료형(Dictionary)

"""
딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요소값을 구하지 않고 Key를 통해서 Value를 얻는다.
이것이 바로 딕셔너리의 가장 큰 특징이다.
basaball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.

"""

# 딕셔너리는 어떻게 만들까?
# {Key1:Value1,Key2:Value2,Key3:Value3}

print('\n딕셔너리는 어떻게 만들까?\n')

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

a = {1: 'hi'}
a = {'a': [1, 2, 3]}

# 딕셔너리 쌍 추가하기, 삭제하기

print('\n딕셔너리 쌍 추가, 삭제하기\n')

# 1.딕셔너리 쌍 추가하기

print('\n딕셔너리 쌍 추가하기\n')

# {1:'a'}라는 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 Key와 Value가 각각 2와
# 'b'인 2:'b'라는 딕셔러니 쌍이 추가된다.

a = {1: 'a'}
a[2] = 'b'
print(a)  # {1:'a',2:'b'}

# 딕셔너리 a에 'name:'pey'라는 쌍이 추가되었다.

a['name'] = 'pey'
print(a)  # {1:'a',2:'b','name':'pey}

# Key는 3, Value는 [1,2,3]을 가지는 한 쌍이 또 추가되었다.

a[3] = [1, 2, 3]
print(a[3])

# 2.딕셔너리 요소 삭제하기
# del 함수를 사용해서 del[key]처럼 입력하면 지정한 key에 해당하는 {key:value} 쌍이 삭제된다.

print('\n딕셔너리 요소 삭제하기\n')

del a[1]
print(a)  # {2:'b','name':'pey',3:[1,2,3]}

# 딕셔너리 요소 삭제하기

# 딕셔너리를 사용하는 방법

print('\n딕셔너리를 사용하는 방법\n')

# 딕셔너리에서 Key 사용해 Value 얻기

print('\n딕셔너리에서 Key 사용해 Value 얻기\n')

grade = {'pey': 10, 'julliet': 99}
grade['pey']
print(grade['pey'])
grade['julliet']
print(grade['julliet'])

a = {1: 'a', 2: 'b'}
a[1]
print(a[1])
a[2]
print(a[2])

a = {'a': 1, 'b': 2}
a['a']
print(a['a'])
a['b']
print(a['b'])

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic['name']
print(dic['name'])
dic['phone']
print(dic['phone'])
dic['birth']
print(dic['birth'])

# 딕셔너리 만들 때 주의할 사항

# 딕셔너리에서 Key는 교유한 값이므로 중복되는 Key값을 설정해 놓으면 하나를 제외한 나머지 것들이 무시된다는 점을 주의해야 한다.
# 동일한 Key가 존재하면 어떤 Key에 해당하는 Value를 불러야 할 지 알 수 없기 때문이다.
# Key에 리스트는 쓸 수 없다.
# 딕셔너리에 쓸 수 있느냐 없느냐는 변할 수 있는 값이냐 변할 수 없는 상수이냐에 따라 달려있다.
# 단 Value에는 변하는 값이든 변하지 않는 값이든 상관없이 아무 값이나 넣을 수 있다.

# 딕셔너리 관련 함수들

print('\n딕셔너리 관련 함수들\n')

# Key 리스트 만들기(keys)

print('\nKey 리스트 만들기(keys)\n')

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
print(a.keys())  # a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys라는 객체를 리턴한다

for k in a.keys() :
    print(k)

list(a.keys())
print(list(a.keys()))

#Value 리스트 만들기(values)
#values 함수는 value의 값을 dict_values 객체로 리턴해준다.

print('\nValue 리스트 만들기\n')

a.values()
print(a.values())

#Key, Value 쌍 얻기(items)
#items 함수는 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴해준다.

print('\nKey, Value 쌍 얻기(items)\n')

a.items()
print(a.items())

#Key:Value 쌍 모두 지우기(clear)
#clear() 함수는 딕셔너리 안의 모든 요소를 삭제한다. 빈 리스트를 [], 빈 튜플을 ()로 표현하는 것과 마찬가지로 빈 딕셔너리도 {}로 표현한다.

print('\nKey:Value 쌍 모두 지우기(clear)\n')

a.clear()
print(a.clear()) # {}

#Key로 Value얻기(get)
#get(x) 함수는 x라는 key에 대응되는 value를 리턴해준다.

print('\nKey로 Value얻기(get)\n')

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.get('name')
print(a.get('name'))

#딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 기본 값을 대신 가져오게 하고 싶을 때에는 get(x, '기본 값')을 사용한다.

a.get('foo','bar')
print(a.get('foo','bar')) # a 딕셔너리에는 'foo'에 해당하는 값이 없다 따라서 기본 값인 'bar'를 리턴한다.

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
#in 함수는 해당 Key가 딕셔너리 안의 존재 유무를 확인한 뒤 참일 경우 boolean type의 자료형 true를 거짓일 경우 false를 리턴한다.

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
'name' in a
print('name' in a)
'email' in a
print('email' in a)
