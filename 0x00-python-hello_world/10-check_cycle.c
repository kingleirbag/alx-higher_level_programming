#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle
 * @list: pointer list argument
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *single_step = list;
	listint_t *double_step = list;

	while ((single_step != NULL) && (double_step != NULL)
			&& (*double_step).next != NULL)
	{
		double_step = double_step->next->next;
		single_step = (*single_step).next;
		if (single_step == double_step)
			return (1);
	}
	return (0);
}
