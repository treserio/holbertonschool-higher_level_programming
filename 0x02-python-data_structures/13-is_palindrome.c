#include "lists.h"
/**
 * is_palindrome - is a singly linked list a palindrome?
 * @head: beginning of single linked list
 * Return: if palindrome 1 else 0
 */
int is_palindrome(listint_t **head)
{
	char array[2000];
	listint_t *temp = *head;
	unsigned int beg = 0, end = 0;

	if (*head == NULL)
		return (1);
	while (temp != NULL)
	{
		array[end] = temp->n;
		temp = temp->next;
		++end;
	}
	--end;
	for (; beg < end; --end, ++beg)
	{
		if (array[beg] != array[end])
			return (0);
	}
	return (1);
}