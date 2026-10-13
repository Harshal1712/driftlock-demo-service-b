import axios from 'axios'
import debounce from 'lodash/debounce'

const client = axios.create({ baseURL: '/api' })

export async function loadInvoice(id) {
  try {
    const { data } = await client.get(`/invoices/${id}`)
    return data
  } catch (err) {
    if (err.response && err.isAxiosError) return null
    throw err
  }
}

export const loadInvoiceDebounced = debounce(loadInvoice, 200)
