#include <stdlib.h>
#include <stdio.h>

#include "stack.h"

link top;
link bottom;
int size = 0;

link stack1=NULL;
link stack2=NULL;

void join(link above, link below) {
	if (below != NULL) below->above = above;
	if (above != NULL) above->below = below;
}


int push(int value)
{
	link new_node;
	size++;
	new_node=(link) malloc(sizeof(stack_list));
	if(!new_node)
	{
		printf("Error\n");
		return 0;
	}

	if (size == 1) bottom = new_node;
	new_node->data=value;
	join(new_node, top);
	top = new_node;
	return 1;
}


int pop()
{
int k;

    if ( ! isEmpty() )
    {
	k = top->data;
	top = top->below;
	if ( top != NULL )
	{
		free(top->above);
		top->above = NULL;
	}
	else
		bottom = top;
	size--;
	return k;
    }
    printf("Stack is empty\n");
    return 0;
}

int isEmpty()
{
	if(size==0)
		return 1;
	else
		return 0;

}

int removeBottom() 
{

		link b = bottom;
		bottom = bottom->above;
		if(bottom!=NULL) 
			bottom->below=NULL;
		size--;

		return b->data;

}

void print_stack()
{
link b = bottom;
	printf("Bottom - up: ");

	while ( b != NULL )
	{
		printf("%d ", b->data);
		b = b->above;
	}
	printf("\n");
}

/** A test method */

void main(int argc, char *argv[])
{
    driver(atoi(argv[1]));
}

