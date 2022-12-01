#include "lists.h"

/**
 * check_cycle - checks if linked list contains a cycle
 * @list: linked list 
 *
 * Return: 1 is list has cycle 0 if not
 */
int  check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
