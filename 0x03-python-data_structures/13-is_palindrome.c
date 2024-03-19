#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse - reverses a linked list
 * @head: double pointer to head role
 * Return: pointer to first node of reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head node
 * Return: 0 if it is not a palindrome, 1 id it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head,
*start_second_half, *prev_slow = *head;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			start_second_half = slow->next;
		}
		else
		{
			start_second_half = slow;
		}
		prev_slow->next = NULL;
		reverse(&start_second_half);

		while (*head && start_second_half)
		{
			if ((*head)->n == start_second_half->n)
			{
				*head = (*head)->next;
				start_second_half = start_second_half->next;
			}
			else
			{
				return (0);
			}
			if (*head == NULL && start_second_half == NULL)
			{
				return (1);
			}
		}
	}
	return (1);
}
