#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints list
 * @h: ptr to head
 * Return: no. of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = currenr->next;
		n++;
	}
	return (n);
}
/**
 * add_nodeint - adds a new node at the beginning of a list
 * @head: ptr to list
 * @n: int to be included in node
 * Return: address of new el or null if it fails 
 */
listint_t *add_nodeint(listint_t **head, const int)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL)
	}
	new->n = n;
	new->next = *head;
	return (new);
}
/**
 * free_listint - frees a list
 * @head: pointr to list
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint *current;

	while (head != NULL)
	{
		current =head;
		head = head-> head->next;
		free(current);
	}
}
