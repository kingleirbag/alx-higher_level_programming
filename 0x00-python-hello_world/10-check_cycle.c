#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle
 * @list: head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while ((slow != NULL) && (fast != NULL) && (*fast).next != NULL)
	{
		fast = fast->next->next;
		slow = (*slow).next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
