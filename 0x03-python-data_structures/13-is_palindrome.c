#include "lists.h"
int is_palindrome(listint_t **head)
{

        listint_t* fast = *head;
        listint_t* slow = *head;

        while(fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }

        int* left = malloc(sizeof(int)*list_length);
        int* right = left + list_length - 1;
  
        while(slow)
        {
            *left++ = slow->n;
            slow = slow->next; 
        }

        while(left < right)
        {
            if(*left != *right)
            {
                free(left);
                return 0;
            }
        left++;
        right--;
        }

        free(left);
        return 1;
}
