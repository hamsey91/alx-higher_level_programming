#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Function that checks if a singly linked list has a cycle.
 *
 * @list: Pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		return (1);
	}
	return (0);
}
