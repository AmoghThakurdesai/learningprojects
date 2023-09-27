/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;
class Node
{
bool value;
    Node *next;
    Node *prev;
    friend class DCLinkedList;
};

class DCLinkedList
{
    Node *head;

public:
    DCLinkedList()
    {
    head = nullptr;

    };
public:
    void insert(bool data, int pos);
    void insertend(bool data);
    void del(int pos);
    void print();
    void change(bool data,int pos);
    void get(int pos);
    Node* gethead();
};

Node* DCLinkedList::gethead()
{return head;}

void DCLinkedList::insert(bool data, int pos)
{
int count = 0;
Node *n = new Node;
n->value = data;
if(head == nullptr)
{
head=n;
n->prev = n->next = head;
}
else
{
if(pos==0)
{
head->prev->next=n;
n->next=head;
n->prev=head->prev;
head->prev=n;
head=n;

}
else
{
Node *k = head;
while(count < pos -1)
{
k=k->next;
count+=1;
}
n->next=k->next;
k->next->prev=n;
k->next=n;
n->prev = k;

}
}
}

void DCLinkedList::insertend(bool data)
{
    Node *h3 = head;
    Node *n2 = new Node;
    n2->value=data;
    while(h3->next!=head)
{

h3 = h3->next;
}
n2->next=head;
n2->prev=h3;
h3->next=n2;
head->prev=n2;

}

void DCLinkedList::del(int pos)
{
    Node *t = head;
    Node *t1;
    if(pos==0){
    t1=head->next;
    delete head;
    head = t1;
}
else{int count2 = 0;

while(count2 < pos - 1 )
{
t=t->next;
count2++;
}
t1 = t->next;
t->next = t1->next;
t1->next->prev=t;
delete t1;}
}

void DCLinkedList::print()
{
Node *h2 = head;
int count3=0;
do
{

cout << h2->value <<"<=>" ;
h2 = h2->next;

}while(h2!=head);
cout<<"\n";
}

void DCLinkedList::change(bool data, int pos)
{
int count2 = 0;
Node *q = head;
Node *q1;
while(count2 < pos)
{
q=q->next;
count2++;
}
q->value = data;
}

void DCLinkedList::get(int pos)
{
int count2 = 0;
Node *q = head;
while(count2 < pos)
{
q=q->next;
count2++;
}
cout << q->value << "n";
}
int main()
{
DCLinkedList cinemax[10];
Node *heads[10];
int op;

for(int i=0;i<10;i++)
{
cinemax[i].insert("0",0);
for(int j=1;j<7;j++)
{
cinemax[i].insertend(0);
heads[i] = cinemax[i].gethead();
}
cinemax[i].print();
}

// do
// {

// cout<<"Enter operation(1 for booking ,2 for cancellation,3 to exit)"<<endl;
// cin >> op;
// switch(op)
// {
// case 1:
//  {

//  }
// break;
// case 2:
// {

// break;
// }while(op<3);

// }

return 0;
}