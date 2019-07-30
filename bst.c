#include <stdio.h>
#include<stdlib.h>
 
struct node
{
    int data;
    struct node* left;
    struct node* right;
};
struct node* createNode(value){
    struct node* newNode = malloc(sizeof(struct node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
  
struct node* insert(struct node* root, int data)
{
    if (root == NULL) return createNode(data);
    if (data < root->data)
        root->left  = insert(root->left, data);
    else if (data > root->data)
        root->right = insert(root->right, data); 
 
    return root;
}
void inorder(struct node* root){
    if(root == NULL) return;
    inorder(root->left);
    printf("%d ->", root->data);
    inorder(root->right);
}
void smallest(struct node *root)
{

    while(root != NULL && root->left != NULL)
    {
        root = root->left;
    }
    printf("%d \n",root->data);
}
void largest(struct node *root)
{

    while(root != NULL && root->right != NULL)
    {
        root = root->right;
    }
    printf("%d \n",root->data);
}
int main(){
    struct node* root=NULL;
    root=insert(root,8);
    insert(root,3);
    insert(root, 1);
    insert(root, 6);
    insert(root, 7);
    insert(root, 10);
    insert(root, 14);
    insert(root, 4);
    inorder(root);
    smallest(root);
    largest(root);
}


