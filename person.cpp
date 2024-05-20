#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		long long int fib();
	private:
		long long int  _fib(long long int);
		int age;
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}
long long int Person::fib()
{
	return _fib (age);
}
long long int Person:: _fib(long long int n)
{
if (n<=1)
{
	return n;
}
else
{
	return _fib(n-1)+_fib(n-2);
}
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	long long int Person_fib(Person*person, long long int n){return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
