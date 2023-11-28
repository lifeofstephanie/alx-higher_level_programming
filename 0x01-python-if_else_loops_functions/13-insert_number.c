#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: head of linked list
 * @number: index to insert
 * Return: the address of the new node, or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *header = *head;

	if (head == NULL || *head == NULL)
                return NULL;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return NULL;
	temp->n = number;
	temp->next = NULL;

	while (header)
	{
		if(temp->n >= header->n && temp->n<(header->next)->n)
		{
			temp->next = header->next;
			header->next = temp;
			break;
		}
		header = header->next;
	}
	return header;
}

