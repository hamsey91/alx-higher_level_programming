#include "lists.h"
#include <string.h>

/**
 * rev_listint - Function to reverse linked list
 *
 * @head: Pointer to pointer of first node of listint_t list
 *
 * Return: Pointer to the first node in the newlist
 */
void rev_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
}

/**
 * is_palindrome - function to checks if a singly linked list is a palindrome.
 *
 * @head: Pointer to pointer of first node of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *mid = *head, *reversed = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
		reversed = slow->next;
		break;
		}
		if (!fast->next)
		{
			reversed = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	rev_listint(&reversed);

	while (reversed && mid)
	{
		if (mid->n == reversed->n)
		{
			reversed = reversed->next;
			mid = mid->next;
		}
		else
			return (0);
	}

	if (!reversed)
	return (1);

	return (0);
}

