"""
Student: Zhiyue Yuan
Mail: yuriyeahyeah@163.com
Reviewed by: Mina
Date: 2023-10-18
"""
#include <cstdlib>
// Person class

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades(); // changed return type from int to double
		long long int fib(); // added for executing fibonacci-calculations
	private:
		int age;
		long long int _fib(long long int); // added for executing fibonacci-calculations, recursive thinking with argument int
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){ // changed return type from int to double
	return double(age)/10.0; // get a float by diving with a float & use double() to round to one decimal precision
	}
long long int Person::fib()
{
	return _fib(age);
}

long long int Person::_fib(long long int n)
{
if (n <= 1)
{
	return n;
}
else
{
	return _fib(n-1) +_fib(n-2);
}
}

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();} // changed return type from int to double
	long long int Person_fib(Person*person, long long int n) {return person->fib();} // added for executing fibonacci-calculations
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
