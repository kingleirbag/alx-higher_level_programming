#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle
 * @list: pointer list argument
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while ((slow != NULL) && (fast != NULL) && (*fast).next != NULL)
	{
		fast = fast->next->next;
		slow = (*slow).next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
