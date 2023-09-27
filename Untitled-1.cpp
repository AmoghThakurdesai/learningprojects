#include <iostream>
#include <queue>
using namespace std;
class node
{
        public:
        int data;
        node* left; node* right;
        friend class bt;
        node(){data=0;left=right=nullptr;};
        // int t1; cout << "Enter data" << endl;
        node(int d){data = d;left=right=nullptr;}
        ~node(){delete left;delete right;cout << "Deleting " << data << endl; }
        
};

class bt
{
private:
node* copy(node* root);
    public:
    node* root;
    bt(){root = nullptr;}
    void insertbfs(int d, node *r);
    void inorderrecur(node* r);
    void search(int d,node *r);
    int min(node* r);
    int max(node* r);
    int heightrecur(node* r);
    void swaprecur(node *r);
    node* maxnode(node *r);
    node* deletenode(int d,node *r);
    void postorder(node* r);
    node* insertroot(int d);
    void erase();
    bt operator = (bt b1);
};

bt bt::operator = (bt b1)
{
    *b1.root = *copy(root);
    return b1;
}


void bt::erase()
{
    if(root==nullptr)
    {
        return;
    }
    delete root;
}

node* bt::copy(node* r)
{
if(r== nullptr)
{
return r;
}
node *temp = new node;
temp->data = r->data;
*temp->left = *copy(r->left);
*temp->right = *copy(r->right);
return temp;
}

node* bt::insertroot(int d)
{
node* temp = new node(d);
if(root==nullptr){
root =  temp; cout << "Root set as " << root->data << endl;
}
else{cout << "Root already present" << endl;}
return root;
}

void bt::inorderrecur(node* r)
{
    if(r==nullptr)
    {return;}
    inorderrecur(r->left);
    cout << r->data << " ";
    inorderrecur(r->right);
}

void bt::insertbfs(int d,node *r)
{
node* temp = new node(d);
node* current = r;
queue<node*> q;
q.push(r);
bool f,f1,f2;
while(!q.empty())
{

if(current->left!=nullptr)
{
q.push(current->left);
}
else
{

cout << "Do you want to insert "<< temp -> data << " at left of " << current->data << endl;
cout << "1 for yes, 0 for no" << endl;
cin >> f1;
if(f1 == 1)
{
current->left = temp;
cout << temp->data << " inserted at left of " << current->data << endl;break;
}
}
if(current->right!=nullptr)
{
q.push(current->right);
}

else

{
bool f2;
cout << "Do you want to insert " << temp->data <<" at right of " << current->data << endl;
cout << "1 for yes, 0 for no" << endl;
cin >> f2;
if(f2 == 1)
{
current->right = temp;
cout << temp->data << " inserted at right of " << current->data << endl;
break;
}

}
if(current!= nullptr)
{
current = q.front();q.pop();
}
};
}

void bt::swaprecur(node *r)
{
    if(r==nullptr)
    {return;}
    node* temp = r->left;
    r->left = r->right;
    r->right = temp;
    swaprecur(r->right);
    swaprecur(r->left);
}

int bt::heightrecur(node *r)
{
    if(r==nullptr){return 0;}
    return 1 + std::max(heightrecur(r->left),heightrecur(r->right));
}
int main()
{
    bt b;
    node* root = b.insertroot(12);
    b.insertbfs(78,root);
    b.insertbfs(23,root);
    b.insertbfs(56,root);
    b.insertbfs(44,root);
    b.insertbfs(38,root);
    b.insertbfs(99,root);
    b.inorderrecur(root);cout << "\n";
    cout << "height of tree is :" << b.heightrecur(root) << endl;
    cout << "COPY\n" << endl;
    bt newtree = b;
    node* copyroot = newtree.root;
    newtree.inorderrecur(copyroot);
    newtree.erase();
    b.inorderrecur(root);
    cout << "Swap:" << endl;
    b.swaprecur(root);
    b.inorderrecur(newtree.root);
    return 0;
}