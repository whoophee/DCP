// This problem was asked by Facebook.
// You have a large array with most of the elements as zero.
// Use a more space-efficient data structure, SparseArray, that implements the same interface:
// •	init(arr, size): initialize with the original large array and size.
// •	set(i, val): updates index at i with val.
// •	get(i): gets the value at index i.
////////
// This problem can be solved using HashMap very easily, but that defeats the purpose of the problem.
#include <functional>
#include <iostream>
#define MAP_SIZE 10
using namespace std;
class Node{
public:
  int val;
  Node *next;
  size_t hash_val;
  Node(size_t hashval, int input_val = 0){
    val = input_val;
    hash_val = hashval;
    next = NULL;
  }
};
// Linked list tailored for HashMap/SparseArray
class LinkedList{
  Node *root;
  Node * search(size_t hashval, bool create_new = true){
    Node *current = root;
    // Create new node if current is null
    if(root == NULL){
      if(create_new){
        root = new Node(hashval);
        return root;
      }
      return NULL;
    }
    while(true){
      // if equal, return relevant node
      if(current-> hash_val == hashval){
        return current;
      }
      // if end is reached, create new or return NULL accordingly
      else if(current->next == NULL){
        if(create_new){
          Node *next = new Node(hashval);
          current->next = next;
          return next;
        }
        else{
          return NULL;
        }
      }
      // traverse rest of the linked list
      else{
        current = current->next;
      }
    }
  }
public:
  LinkedList(){
    root = NULL;
  }
  void search_set(size_t hashval, int input_val){
    Node *tmp = search(hashval);
    tmp->val = input_val;
  }
  int search_get(size_t hashval){
    // cout<<"Searching for "<<hashval<<endl;
    Node *tmp = search(hashval, false);
    if(tmp == NULL){
      // cout<<"Got NULL"<<endl;
      return 0;
    }
    return tmp->val;
  }
};
// The hash function is used here effectively translates to an identity function (as implemented in C++)
// Directly using the index would suffice. For now, the idea that this solution is similar to the implementation
// of a hash table is enforced.
class SparseArray{
  LinkedList l[MAP_SIZE];
  hash<int> get_hash;
  int size;
public:
  void set(int i, int val){
    if(i < 0 || i >= size){
      throw "Array index out of bounds";
    }
    if(val == 0)
      return;
    size_t h = get_hash(i);
    l[h % MAP_SIZE].search_set(h, val);
  }
  int get(int i){
    if(i < 0 || i >= size){
      throw "Array index out of bounds";
    }
    size_t h = get_hash(i);
    return l[h % MAP_SIZE].search_get(h);
  }
  void init(int *arr, int len){
    for(int i = 0; i < len; i++){
      if(*(arr+i)){
        set(i, *(arr+i));
      }
    }
  }
};

int main(){
  int input[] = {0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 0, 0, 3, 6, 7, 10, 0, 0, 11, 0, 0, 1};
  int len = 22;
  SparseArray s;
  s.init(input, len);
  cout<<s.get(15)<<endl;
  s.set(15, 12);
  cout<<s.get(15)<<endl;
  cout<<s.get(0)<<endl;
  cout<<s.get(21)<<endl;
}
