#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if a singly linked listhas a cycle
 * @list: pointer to list
 * Return: 0 success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
