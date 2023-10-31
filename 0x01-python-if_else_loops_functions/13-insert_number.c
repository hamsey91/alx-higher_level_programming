#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *prev = NULL, *new = malloc(sizeof(listint_t));

	if (new == NULL)
	return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (node && node->n < number)
	{
		prev = node;
		node = node->next;
	}

	new->next = node;

	if (prev == NULL)
		*head = new;
	else
		prev->next = new;

	return (new);
}
