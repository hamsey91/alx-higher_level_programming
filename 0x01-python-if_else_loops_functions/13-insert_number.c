#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts number into sorted singly linked list
 *
 * @head: Pointer the head of the linked list
 * @number: The inserted number
 *
 * Return: NULL if failed, address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
	return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
	new->next = *head;
	*head = new;
	return (new);
	}

	while (node->next && node->next->n < number)
	node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
