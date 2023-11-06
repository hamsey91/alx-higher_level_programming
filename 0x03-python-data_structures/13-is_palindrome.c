#include "lists.h"

/**
 * add_nodeint_start - adds a new node at the start of a listint_t list
 *
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 *
 * Return: address of the new element, or NULL if it fails
*/

listint_t *add_nodeint_start(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome.
 *
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *n_head = *head;
	listint_t *rev_list = NULL, *rev_ptr = NULL;

	if (*head == NULL || n_head->next == NULL)
		return (1);
	while (n_head != NULL)
	{
		add_nodeint_start(&rev_list, n_head->n);
		n_head = n_head->next;
	}
	rev_ptr = rev_list;
	while (*head != NULL)
	{
		if ((*head)->n != rev_ptr->n)
		{
			free_listint(rev_list);
			return (0);
		}
		*head = (*head)->next;
		rev_ptr = rev_ptr->next;
	}

	free_listint(rev_list);
	return (1);
}
